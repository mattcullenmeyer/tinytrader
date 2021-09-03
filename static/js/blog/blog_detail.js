// https://docs.djangoproject.com/en/3.1/ref/csrf/
const csrftoken = Cookies.get('csrftoken');

document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('#comment-form').addEventListener('submit', async (event) => {
    // https://www.valentinog.com/blog/form-data/
    event.preventDefault();
    const form = event.currentTarget;
    url = form.action;
    const formData = new FormData(form);
    const entries = formData.entries();
    const data = Object.fromEntries(entries);

    const response = await fetch(
      url,
      {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
          'X-CSRFToken': csrftoken,
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          content: data,
        })
      }
    );

    if (response.status === 201) {
      const jsonResponse = await response.json();
      
      // clear comment input of form
      document.querySelector('#comment-input').value = '';

      const commentSection = document.querySelector('#comment-section');
      const newComment = document.createElement('div');

      const { 
        newCommentId, 
        newCommentName, 
        newCommentCreatedOn,
        newCommentBody, 
      } = jsonResponse;

      newCommentCreatedOnFormatted = formatDate(newCommentCreatedOn);

      newComment.innerHTML = `
        <div id="comment-${newCommentId}" class="comment-card">
          <div class="comment-card-width-full">
            <div>
              <h5 class="card-title comment-card-username">${newCommentName}</h5>
              <h6 class="card-text comment-card-date">${newCommentCreatedOnFormatted}</h6>
              <p class="card-text comment-card-body">${newCommentBody}</p>
            </div>
            <div class="dropdown-divider"></div>
          </div>
        </div>
      `;
      commentSection.append(newComment);
    };
  });
});

const formatDate = (rawDate) => {
  const date = new Date(rawDate);
  const formattedDate = date.toLocaleString('default', 
    { month: 'short', day: 'numeric', year: 'numeric' }
  );
  return formattedDate;
};
