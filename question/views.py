import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from question.forms import QuestionForm, ChoiceForm, QuestionForm2, ChoiceForm2, QuestionForm3, ChoiceForm3, \
    QuestionForm4, QuestionForm5, ChoiceForm5, ChoiceForm4
from question.models import Question, Choice, Question2, Choice2, Category, Question3, Choice3, Question4, Choice4, \
    Question5, Choice5


# Create your views here

def top(request):
    #request.session.clear()
    return render(request, 'question/top.html')


def category(request):
    return render(request, 'question/category.html')


def question(request):
    question_session = request.session.setdefault('question_count', 1)
    question_categoryid_get = Question.objects.filter(question_category=1).all().order_by('create_at')
    question_list = list(question_categoryid_get)
    a = len(question_list)
    answered_questions = request.session.get('answered_questions', [])
    unanswered_questions = [q for q in question_categoryid_get if q.id not in answered_questions]

    if unanswered_questions:
        random_question = random.choice(unanswered_questions)
        answered_questions.append(random_question.id)
        request.session['answered_questions'] = answered_questions
    else:
        random_question = None

    correct_count = request.session.get('correct_count', 0)
    if question_session >= 10:
        request.session['answered_questions'] = []
        request.session['question_count'] = 1
        return render(request, 'question/result.html', {'correct_count': correct_count})
    q = Question.objects.filter(id=question_session).all()
    q = q[0]
    choices = Choice.objects.filter(choice_to=random_question).all().order_by('?')
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice, pk=str(selected_choice_id))
        select = selected_choice.__str__()
        answer = selected_choice.choice_to.answer
        if choices:
            request.session.setdefault('correct_count', 0)
            feedback = '正解です' if answer == select else '不正解です'  # select_choiceには選択した文字列が入る
            feadback2 = select
            request.session['question_count'] += 1
            if answer == select:
                request.session['correct_count'] += 1

        else:
            feedback = "クイズがありません。"

        return render(request, 'question/next/next.html',
                      {'question': q, 'feedback': feedback, 'feadback2': feadback2, 'answer': answer})
    else:
        feedback = None

    return render(request, "question/question_a.html",
                  {'questions': q, 'choices': choices, 'feedback': feedback, 'correct_count': correct_count,
                   'count': question_session, 'ran':random_question})


def question2(request):
    question_session = request.session.setdefault('question_count', 0)
    question_categoryid_get = Question2.objects.filter(question_category=2).all().order_by('create_at')
    question_list = list(question_categoryid_get)
    a = len(question_list)
    b = random.uniform(1, a)
    q = Question2.objects.filter(id=b).all()
    q = q[0]
    correct_count = request.session.get('correct_count', 0)
    if question_session >= a:
        request.session['question_count'] = 0
        return render(request, 'question/result.html', {'correct_count': correct_count})
    question = question_list[question_session]

    choices = Choice2.objects.filter(choice_to=b).all().order_by('?')

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice2, pk=str(selected_choice_id))
        select = selected_choice.__str__()
        answer = selected_choice.choice_to.answer

        if choices:
            request.session.setdefault('correct_count', 0)
            feedback = '正解です' if answer == select else '不正解です'  # select_choiceには選択した文字列が入る
            request.session['question_count'] += 1
            if answer == select:
                request.session['correct_count'] += 1

        else:
            feedback = "クイズがありません。"

        return render(request, 'question/next/next2.html', {'question': question, 'feedback': feedback})
    else:
        feedback = None

    return render(request, "question/question_a.html",
                  {'questions': q, 'choices': choices, 'feedback': feedback, 'correct_count': correct_count})


def question3(request):
    question_session = request.session.setdefault('question_count', 0)
    question_categoryid_get = Question3.objects.filter(question_category=3).all().order_by('create_at')
    question_list = list(question_categoryid_get)
    a = len(question_list)
    b = random.uniform(1, a)
    q = Question3.objects.filter(id=b).all()
    q = q[0]
    correct_count = request.session.get('correct_count', 0)
    if question_session >= a:
        request.session['question_count'] = 0
        return render(request, 'question/result.html', {'correct_count': correct_count})
    question = question_list[question_session]

    choices = Choice3.objects.filter(choice_to=b).all().order_by('?')

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice3, pk=str(selected_choice_id))
        select = selected_choice.__str__()
        answer = selected_choice.choice_to.answer

        if choices:
            request.session.setdefault('correct_count', 0)
            feedback = '正解です' if answer == select else '不正解です'  # select_choiceには選択した文字列が入る
            request.session['question_count'] += 1
            if answer == select:
                request.session['correct_count'] += 1

        else:
            feedback = "クイズがありません。"

        return render(request, 'question/next/next3.html', {'question': question, 'feedback': feedback})
    else:
        feedback = None

    return render(request, "question/question_a.html",
                  {'questions': q, 'choices': choices, 'feedback': feedback, 'correct_count': correct_count})


def question4(request):
    question_session = request.session.setdefault('question_count', 0)
    question_categoryid_get = Question4.objects.filter(question_category=4).all().order_by('create_at')
    question_list = list(question_categoryid_get)
    a = len(question_list)
    b = random.uniform(1, a)
    q = Question4.objects.filter(id=b).all()
    q = q[0]
    correct_count = request.session.get('correct_count', 0)
    if question_session >= a:
        request.session['question_count'] = 0
        return render(request, 'question/result.html', {'correct_count': correct_count})
    question = question_list[question_session]

    choices = Choice4.objects.filter(choice_to=b).all().order_by('?')

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice4, pk=str(selected_choice_id))
        select = selected_choice.__str__()
        answer = selected_choice.choice_to.answer

        if choices:
            request.session.setdefault('correct_count', 0)
            feedback = '正解です' if answer == select else '不正解です'  # select_choiceには選択した文字列が入る
            request.session['question_count'] += 1
            if answer == select:
                request.session['correct_count'] += 1

        else:
            feedback = "クイズがありません。"

        return render(request, 'question/next/next.html', {'question': question, 'feedback': feedback})
    else:
        feedback = None

    return render(request, "question/question_a.html",
                  {'questions': q, 'choices': choices, 'feedback': feedback, 'correct_count': correct_count})


def question5(request):
    question_session = request.session.setdefault('question_count', 0)
    question_categoryid_get = Question5.objects.filter(question_category=5).all().order_by('create_at')
    question_list = list(question_categoryid_get)
    a = len(question_list)
    b = random.uniform(1, a)
    q = Question5.objects.filter(id=b).all()
    q = q[0]
    correct_count = request.session.get('correct_count', 0)
    if question_session >= a:
        request.session['question_count'] = 0
        return render(request, 'question/result.html', {'correct_count': correct_count})
    question = question_list[question_session]

    choices = Choice5.objects.filter(choice_to=b).all().order_by('?')

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice5, pk=str(selected_choice_id))
        select = selected_choice.__str__()
        answer = selected_choice.choice_to.answer

        if choices:
            request.session.setdefault('correct_count', 0)
            feedback = '正解です' if answer == select else '不正解です'  # select_choiceには選択した文字列が入る
            request.session['question_count'] += 1
            if answer == select:
                request.session['correct_count'] += 1

        else:
            feedback = "クイズがありません。"

        return render(request, 'question/next/next5.html', {'question': question, 'feedback': feedback})
    else:
        feedback = None

    return render(request, "question/question_a.html",
                  {'questions': q, 'choices': choices, 'feedback': feedback, 'correct_count': correct_count})


@login_required
def question_new(request, category_id):
    initial_value = {"question_category": category_id}
    if request.method == 'POST':
        form = QuestionForm(request.POST, initial_value)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.create_by = request.user
            question_form.save()
            return redirect(choice_new, question_id=question_form.pk)
    else:
        form = QuestionForm(initial_value)
    return render(request, "question/new/question_new.html", {'form': form})


@login_required
def question_new2(request, category_id):
    initial_value = {"question_category": category_id}
    if request.method == 'POST':
        form = QuestionForm2(request.POST, initial_value)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.create_by = request.user
            question_form.save()
            return redirect(choice_new2, question_id=question_form.pk)
    else:
        form = QuestionForm2(initial_value)
    return render(request, "question/new/question_new2.html", {'form': form})


@login_required
def question_new3(request, category_id):
    initial_value = {"question_category": category_id}
    if request.method == 'POST':
        form = QuestionForm3(request.POST, initial_value)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.create_by = request.user
            question_form.save()
            return redirect(choice_new3, question_id=question_form.pk)
    else:
        form = QuestionForm3(initial_value)
    return render(request, "question/new/question_new3.html", {'form': form})

@login_required
def question_new4(request, category_id):
    initial_value = {"question_category": category_id}
    if request.method == 'POST':
        form = QuestionForm4(request.POST, initial_value)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.create_by = request.user
            question_form.save()
            return redirect(choice_new4, question_id=question_form.pk)
    else:
        form = QuestionForm4(initial_value)
    return render(request, "question/new/question_new4.html", {'form': form})


@login_required
def question_new5(request, category_id):
    initial_value = {"question_category": category_id}
    if request.method == 'POST':
        form = QuestionForm5(request.POST, initial_value)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.create_by = request.user
            question_form.save()
            return redirect(choice_new5, question_id=question_form.pk)
    else:
        form = QuestionForm5(initial_value)
    return render(request, "question/new/question_new5.html", {'form': form})


def choice_new(request, question_id):
    initial_values = {"choice_to": question_id}
    question_session = request.session.setdefault('post_count', 0)
    if question_session >= 4:
        request.session['post_count'] = 0
        return redirect(top)
    if request.method == 'POST':
        request.session['post_count'] += 1
        form = ChoiceForm(request.POST, initial_values)
        if form.is_valid():
            choice_form = form.save(commit=False)
            choice_form.save()
            return redirect(choice_new, question_id)
    else:
        form = ChoiceForm(initial_values)
    return render(request, "question/new/choice_new.html", {'form': form})


def choice_new2(request, question_id):
    initial_values = {"choice_to": question_id}
    question_session = request.session.setdefault('post_count', 0)
    if question_session >= 4:
        request.session['post_count'] = 0
        return redirect(top)
    if request.method == 'POST':
        request.session['post_count'] += 1
        form = ChoiceForm2(request.POST, initial_values)
        if form.is_valid():
            choice_form = form.save(commit=False)
            choice_form.save()
            return redirect(choice_new2, question_id)
    else:
        form = ChoiceForm2(initial_values)
    return render(request, "question/new/choice_new2.html", {'form': form, 'a':initial_values})


def choice_new3(request, question_id):
    initial_values = {"choice_to": question_id}
    question_session = request.session.setdefault('post_count', 0)
    if question_session >= 4:
        request.session['post_count'] = 0
        return redirect(top)
    if request.method == 'POST':
        request.session['post_count'] += 1
        form = ChoiceForm3(request.POST, initial_values)
        if form.is_valid():
            choice_form = form.save(commit=False)
            choice_form.save()
            return redirect(choice_new3, question_id)
    else:
        form = ChoiceForm3(initial_values)
    return render(request, "question/new/choice_new3.html", {'form': form, 'a':initial_values})


def choice_new4(request, question_id):
    initial_values = {"choice_to": question_id}
    question_session = request.session.setdefault('post_count', 0)
    if question_session >= 4:
        request.session['post_count'] = 0
        return redirect(top)
    if request.method == 'POST':
        request.session['post_count'] += 1
        form = ChoiceForm4(request.POST, initial_values)
        if form.is_valid():
            choice_form = form.save(commit=False)
            choice_form.save()
            return redirect(choice_new4, question_id)
    else:
        form = ChoiceForm4(initial_values)
    return render(request, "question/new/choice_new4.html", {'form': form, 'a':initial_values})


def choice_new5(request, question_id):
    initial_values = {"choice_to": question_id}
    question_session = request.session.setdefault('post_count', 0)
    if question_session >= 4:
        request.session['post_count'] = 0
        return redirect(top)
    if request.method == 'POST':
        request.session['post_count'] += 1
        form = ChoiceForm5(request.POST, initial_values)
        if form.is_valid():
            choice_form = form.save(commit=False)
            choice_form.save()
            return redirect(choice_new5(), question_id)
    else:
        form = ChoiceForm5(initial_values)
    return render(request, "question/new/choice_new5.html", {'form': form})


def next(request):
    return render(request, 'question/question.html')


def result(request):
    return render(request, 'question/result.html')
