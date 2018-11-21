function sendXML(){
    const xml = document.getElementById('xml').value;
    strip({xml});
}
function sendURL(){
    let url = document.getElementById('url').value;
    if (!url){
        document.getElementById('text').innerText = 'No url';
        return;
    }
    if (!url.startsWith('http')){
        url = `http://${url}`;
    }
    strip({url})
}
function strip(body){
    fetch('/strip', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
    .then(res=>res.text())
    .then(text=>{
        document.getElementById('text').innerText = text
    });
}