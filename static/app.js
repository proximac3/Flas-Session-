// Guess word Submission form
const form = document.querySelector('.word-form')
//  Submit form button
const submitFormButton = document.querySelector('#submit_guess-word')
// Response variable
const $response = $('.response')[0]
// Current Score
const $highScore = $('.score')[0]
// countdown 
const countdown =  $('.time')[0]
// HighScore
const highScoreSelector = $('.highest-score-number')[0]


// Current Score
let currentSccore = 0;

//  Highscore
let highscore = 0

// countdown timer 
let timeLeft = 10

// Numner of imes the user has played the gamm(send to back end)
const NumberOfTimesPlayed = 1


// update count down timer and stop game when time hit 0. 
let intreval =  setInterval(async function () {
    if (timeLeft > 0) {
        countdown.innerText = timeLeft -= 1
    } else {
        // stop game when timer ends
        $response.innerText = `Time's Up`
        
        // Update high Score
        highscore = currentSccore
        highScoreSelector.innerText = highscore
        
        // send high score and number of times played to back end
        const response1 = await axios.post('http://127.0.0.1:5000/update',
            { 'high Score': `${highscore}`, 'times played': `${NumberOfTimesPlayed}` })
        
        console.log(response1)

        // stop interval
        clearInterval(intreval)
    }
}, 1000)



form.addEventListener('click', async function (e) {
    e.preventDefault()

    // chek if timer is up.
    if (timeLeft > 0) {
        if (e.target.getAttribute('id') === 'submit_guess-word') {
            // Guess word
            const inputWord = $('.word-form input').val()
    
            // Ajax request
            const response = await axios.post('http://127.0.0.1:5000/words',
                { 'word': `${inputWord}` })
            
                
                // append results to DOM
                $response.innerText = response.data.results
                
                // check if guess was correct and update current score
                if (response.data.results === 'ok') {
                    let newScore = parseInt($highScore.innerText)
                    newScore += inputWord.length
                    $highScore.innerText = newScore
                    currentSccore++
                    console.log(response)
            }
            
        }   
    }

})
