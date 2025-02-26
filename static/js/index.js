let usernameField=document.getElementById('id_username')
// console.log(usernameField);

usernameField.addEventListener('keyup',(e)=>{
    usernameValue=e.target.value
        fetch('/uservalidate/',{
            body:JSON.stringify({
                username:usernameValue,
            }),
            method:'POST',
        }).then(res=>res.json()).then(data=>{
            let msg=document.querySelector('.msg')
            if(data.user_name_error){
                msg.innerText=data.user_name_error.trim();
                msg.classList.remove('hidden');
                
            }
            else{
                if (!msg.classList.contains('hidden')){
                    msg.classList.add('hidden');
                }
                
            }
        })
    
})
