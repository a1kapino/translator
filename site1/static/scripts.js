let translationIndex = 1;
let source_lang = '';

async function fetchJoke() {
    const response = await fetch('/api/joke');
    const data = await response.json();
    const input = document.getElementById('main-input');
    input.value = data.joke;
    source_lang = 'en';
    const secondaryAction = document.getElementById('secondary-action');
    secondaryAction.innerHTML = '';
    translationIndex = 1;
    const originalInput = document.getElementById('original-input');
    originalInput.classList = 'grey-buttons';
    //const originalUS = document.getElementById('joke-input');
    //originalUS.classList = 'colorful';
    //addLanguageSelection(0);
}

async function fetchNews(country, lang) {
    const response = await fetch(`/api/news?country=${country}&lang=${lang}`);
    const data = await response.json();
    const input = document.getElementById('main-input');
    input.value = data.yournews;
    source_lang = lang;
    const secondaryAction = document.getElementById('secondary-action');
    secondaryAction.innerHTML = '';
    translationIndex = 1;
    const originalInput = document.getElementById('original-input');
    originalInput.classList = 'colorful';
    //const newsLink = document.getElementById('news-link')
    //newsLink.href = 
    const originalUS = document.getElementById('joke-input');
    originalUS.classList = 'grey-buttons';
    //addLanguageSelection(0);  
}

async function translateAndAppend(buttonIndex, source, dest) {
    let currentTransation1 = '';
    let currentTransation2 = '';
    let currentTransation3 = '';
    if (translationIndex === 1) {
        const input = document.getElementById('main-input');
        currentTransation1 = input.value;
        currentTransation2 = input.value;
        currentTransation3 = input.value;
    } else {
        currentTransation1 = document.getElementById(`translation-section-${translationIndex}-1`).innerText;
        currentTransation2 = document.getElementById(`translation-section-${translationIndex}-2`).innerText;
        currentTransation3 = document.getElementById(`translation-section-${translationIndex}-3`).innerText;
    }
    
    const response = await fetch(`/api/translate?input=${currentTransation1}&source=${source}&dest=${dest}`);
    const response2 = await fetch(`/api/translate2?input=${currentTransation2}&source=${source}&dest=${dest}`);
    const response3 = await fetch(`/api/translate3?input=${currentTransation3}&source=${source}&dest=${dest}`);
    /*
    if (buttonIndex == 0) {
        const destUS = 'en-US'
        const response3 = await fetch(`/api/translate3?input=${currentTransation3}&source=${source}&dest=${destUS}`);
    } else {
        const response3 = await fetch(`/api/translate3?input=${currentTransation3}&source=${source}&dest=${dest}`);        
    }
     */   
    const data = await response.json();
    const data2 = await response2.json();  
    const data3 = await response3.json();
    
    translationIndex++;
    const translationHtml = `
 <div class="container">
    <div class="flex-1">
        <div class="mt-1" id="translation-section-${translationIndex}-1">${data.translated}</div> 
    </div>
    <div class="flex-1"  >
        <div class="mt-1" id="translation-section-${translationIndex}-2">${data2.translated2}</div> 
    </div>  
    <div class="flex-1">
        <div class="mt-1" id="translation-section-${translationIndex}-3">${data3.translated3}</div> 
    </div>
</div>
    `;
    source_lang = dest;
    const secondaryAction = document.getElementById('secondary-action');
    secondaryAction.innerHTML += translationHtml;
    addLanguageSelection(buttonIndex);
}


function addLanguageSelection(buttonIndex) {
    const html = `
<div class="center mt-1">
    <div id="lang-selection-${translationIndex}">
        <img onclick="translateAndAppend(0, source_lang,'en')" src="/static/usa.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(1, source_lang,'de')" src="/static/germany.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(2, source_lang,'en')" src="/static/britain.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(3, source_lang,'fr')" src="/static/france.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(4, source_lang,'es')" src="/static/spain.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(5, source_lang,'it')" src="/static/italy.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(6, source_lang,'uk')" src="/static/ukraine.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(7, source_lang,'pl')" src="/static/poland.png" width="42" height="22" class="language">
        <img onclick="translateAndAppend(8, source_lang,'ru')" src="/static/russia2.jpg" width="42" height="22" class="language">
    </div>
</div>
    `;
    const secondaryAction = document.getElementById('secondary-action');
    secondaryAction.innerHTML += html;
    
    const previousRow = document.getElementById(`lang-selection-${translationIndex - 1}`);
    if (previousRow) {
        previousRow.classList += 'grey-buttons';
        const currentRow = document.getElementById(`lang-selection-${translationIndex - 1}`);
        const clickedButton = currentRow.children.item(buttonIndex);
        clickedButton.classList += 'colorful';
    }
}
