document.addEventListener('DOMContentLoaded', () => {
  const pollsContainer = document.getElementById('polls-container');

  fetch('https://ваш-бэкенд.onrender.com/api/polls')
    .then(response => response.json())
    .then(polls => {
      polls.forEach(poll => {
        const pollCard = document.createElement('div');
        pollCard.className = 'poll-card';
        pollCard.innerHTML = `
          <div class="poll-option" 
               style="background-image: url('${poll.image1 || 'https://via.placeholder.com/300'}')">
            <span>${poll.option1}</span>
          </div>
          <div class="poll-option" 
               style="background-image: url('${poll.image2 || 'https://via.placeholder.com/300'}')">
            <span>${poll.option2}</span>
          </div>
        `;
        pollsContainer.appendChild(pollCard);
      });
    });
});
