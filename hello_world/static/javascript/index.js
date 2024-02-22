
let objects=document.querySelectorAll(".update-item");

for( let i=0;i<objects.length;i++){


    objects[i].addEventListener('click',function(){

        sender(this.dataset.id,this.dataset.action);
    })
}

function sender(id,action="add") {
    url='/update-item/'
    fetch(url,{
        'method':'post',
        'headers':{
            'content-type':'application/json',
            'X-CSRFToken':csrf
        },
        'body':JSON.stringify({
            'id':id,
            'action':action,
        })
    }).then(function(response){
        return response.json()
    }).then((data)=>{
       
        window.location.reload()
    })
}
