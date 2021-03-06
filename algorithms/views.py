import json
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Project
from .models import Report
from .algorithms import TFIDFCosineSimilarity, word2VecCosineSimilarity


# Create your views here.
def similarity_algorithms(request, pk):
    project = get_object_or_404(Project, pk=pk)
    reports = Report.objects.filter(project_id=pk)
    content = {
        'project': project,
        'reports': reports,
        'title': f'Document Similarity - {project.title}'
    }
    return render(request, 'pages/algorithms/algorithms_list.html', content)


def apply_similarity_algorithm(request, pk, algorithm):
    project = get_object_or_404(Project, pk=pk)
    reports = Report.objects.filter(project_id=pk, algorithm=algorithm.lower())
    content = {
        'project': project,
        'algorithm': algorithm,
        'reports': reports,
        'files': project.get_files(),
        'title': f'{algorithm.upper()} - {project.title}'
    }
    if request.method == 'POST':
        selected_file_id = int(request.POST['file'])
        files = project.get_files()
        corpus = []
        index = 0
        selected_document_index = 0
        selected_document_name = 0
        for file in files:
            if file.id == selected_file_id:
                selected_document_index = index
                selected_document_name = file.filename()
            index += 1

            file_read = open(file.file.path, "r", encoding='utf8')
            lines = file_read.read()
            file_read.close()
            corpus.append(lines)

        if algorithm.lower() == 'tfidf-cos':
            outputs = TFIDFCosineSimilarity(selected_document_index, corpus)
        elif algorithm.lower() == 'word2vec-cos':
            if word2VecCosineSimilarity(selected_document_index, corpus) is None:
                outputs = None
            else:
                outputs = word2VecCosineSimilarity(selected_document_index, corpus)
        elif algorithm.lower() == 'plagiarism':
            if word2VecCosineSimilarity(selected_document_index, corpus) is None:
                outputs = None
            else:
                outputs = []
                temp_output = []
                output1 = TFIDFCosineSimilarity(selected_document_index, corpus)
                output2 = word2VecCosineSimilarity(selected_document_index, corpus)
                for(item1, item2) in zip(output1, output2):
                    temp_output.append(item1 + item2)
                for index in temp_output:
                    b = index[1] + index[3]
                    c = [index[0], b/2]
                    outputs.append(c)
                
        content['outputs'] = outputs
        content['selected_document_index'] = selected_document_index

        report = Report()
        report.project = project
        report.algorithm = algorithm.lower()
        report.all_data = json.dumps(outputs, separators=(',', ':'))
        report.selected_document_index = selected_document_index
        report.selected_document_name = selected_document_name
        report.save()

        return redirect('view_similarity_report', project.id, algorithm, report.id)

    return render(request, 'pages/algorithms/parameters.html', content)


def view_similarity_report(request, project_pk, algorithm, report_pk):
    project = get_object_or_404(Project, pk=project_pk)
    report = get_object_or_404(
        Report, pk=report_pk, algorithm=algorithm.lower())
    files = project.get_files()

    content = {
        'project': project,
        'algorithm': algorithm,
        'files': files,
        'report': report,
        'selected_document_index': report.selected_document_index,
        'outputs': report.get_output(),
        'title': f'{algorithm.upper()} Report - {project.title}'
    }

    return render(request, 'pages/algorithms/report.html', content)
