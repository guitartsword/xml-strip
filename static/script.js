function sendXML(){
    let url = document.getElementById('url').value;
    const xml = document.getElementById('xml').value;
    if (url && !url.startsWith('http')){
        url = `http://${url}`;
    }
    fetch('/strip', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            url,
            xml
        })
    })
    .then(res=>res.text())
    .then(text=>{
        document.getElementById('text').innerText = text
    });
}