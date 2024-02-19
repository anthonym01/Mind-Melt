//test s stuff
document.getElementById('testpost_btn').addEventListener('click', function () {
    var what = JSON.stringify({ text: document.getElementById('postablegarbage').value })
    console.log('Test post to server ', what)
    post(what, 'post/test')
})

document.getElementById('postablegarbage').addEventListener('change', function () {
    document.getElementById('testpost_btn').title = 'post: ' + document.getElementById('postablegarbage').value
})

document.getElementById('testget_btn').addEventListener('click', function () {
    console.log('Test get from server')
    request('get/test')
})
