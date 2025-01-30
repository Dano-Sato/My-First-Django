// CSRF 토큰을 meta 태그에서 가져오는 함수
function getCSRFToken() {
    token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    console.log("CSRF Token: ", token);
    return token;
}

function deletePost(postId) {
    if (confirm('本当に削除しますか？')) {
        fetch(`/post/${postId}/delete/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),  // CSRF 토큰을 헤더에 추가
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: postId })  // 요청 본문에 데이터를 추가 (필요 시)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                // 성공시 해당 게시물 DOM 요소 삭제
                document.getElementById(`post-${postId}`).remove();
            } else {
                alert(data.error);
            }
        })
        .catch(error => {
            alert('エラーが発生しました');
        });
    }
}