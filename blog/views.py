from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .models import Posting, Reply
from .forms import PostingForm, ReplyForm

# Create your views here.

@require_http_methods(['GET', 'POST'])
def create_posting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save()
            return redirect('blog:posting_detail', posting.pk)
    
    # elif request.method == 'GET':
    else:
        form = PostingForm()

    return render(request, 'blog/form.html', {
        'form':form,
    })

# @require_http_methods(['GET', 'HEAD])
@require_safe
def posting_index(request):
    postings = Posting.objects.all()
    
    return render(request, 'blog/index.html', {
        'postings':postings
    })

@require_safe
def posting_detail(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    # 댓글 index도 posting_detail에서 진행.
    # replies = Reply.objects.all()
    replies = posting.reply_set.all()  # _set 하위 데이터를 가져온다.
    # 댓글 create도 posting_detail 페이지에서 진행.
    form = ReplyForm()

    return render(request, 'blog/detail.html', {
        'posting': posting,
        'replies': replies,
        'form': form,
    })

@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    
    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect('blog:posting_detail', posting.pk)
    # elif request.method == 'GET':
    else:
        form = PostingForm(instance=posting)

    return render(request, 'blog/form.html', {
        'form':form,
    })

@require_POST
def delete_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    posting.delete()

    return redirect('blog:posting_index')

@require_POST
def create_reply(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)  # 저장 중지. forms.py를 보면 content만 가져왔다. 전체를 가져오면 구분이 안 되기 때문이다.
        reply.posting = posting  # FK 직접 삽입
        reply.save()
        return redirect('blog:posting_detail', posting.pk)
    '''
    else:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('댓글 에러')

        return render(request, 'blog/detail.html', {
            'form': form,
            'posting': posting,
            'replies': posting.reply_set.all(),
        })
        
    '''


@require_POST
def delete_reply(request, posting_pk, reply_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    reply.delete()

    return redirect('blog:posting_detail', posting.pk)