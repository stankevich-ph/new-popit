function openComment(article_id){
  let element = document.getElementById('article-' + article_id +'_comments');
  let display = element.style.display;
  if (display === "none" || display === ""){
    element.style.display = "block";
  } else {
    element.style.display = "none"
  }
}


let comment_buttons = document.querySelectorAll(".comment_button");

for (let i=0; i<comment_buttons.length; i++) {
  let comm_btn = comment_buttons[i];
  comm_btn.addEventListener('click', () => openComment(comm_btn.getAttribute("data-news_id")))
}


let like_buttons = document.querySelectorAll(".like_btn");

for (let i=0; i < like_buttons.length; i++) {
  let btn = like_buttons[i];
  let news_id = btn.getAttribute("data-news_id");

  btn.addEventListener('click', () => {
    let request = new XMLHttpRequest();
    request.open("POST", "/news/" + news_id + "/like_action/", true);
    request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);

    request.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        // Response
        let news_likes_count_elem = document.getElementById("news-" + news_id + "_likes_count");
        let current_count = parseInt(news_likes_count_elem.innerText);
        let response = this.responseText;

        if (response === "1") {
          news_likes_count_elem.innerText = (current_count + 1).toString();
        } else if (response === "0") {
          news_likes_count_elem.innerText = (current_count - 1).toString();
        }
      } else if (this.readyState === 4 && this.status === 403) {
        alert(this.responseText)
      }
    };
    request.send()
  })
}