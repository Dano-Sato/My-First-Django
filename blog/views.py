from django.shortcuts import render, redirect, get_object_or_404    
from .forms import PostForm
from .models import Post
from django.views.decorators.http import require_http_methods, require_POST
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required  # 로그인한 사용자만 접근 가능 (아직 사용 안함)
@require_http_methods(["GET", "POST"])  # GET과 POST 메소드만 허용
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required
@require_POST  # POST 메소드만 허용
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 추가 보안 체크
    if not request.user.is_authenticated:
        return JsonResponse({'error': '권한이 없습니다.'}, status=403)
        
    try:
        post.delete()
        return JsonResponse({'message': '削除しました'})
    except Exception as e:
        return JsonResponse({'error': '削除に失敗しました'}, status=400)