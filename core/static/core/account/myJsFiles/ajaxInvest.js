     

    var wraps =document.getElementById("ajax-invest" )

 const getCookie=(name)=> {
    let cookieValue = null;
       if (document.cookie && document.cookie !== ''){
           const cookies = document.cookie.split(';');
           for(let i=0; i<cookies.length; i++){
               const cookie = cookies[i].trim();
               if (cookie.substring(0, name.length + 1) === (name + '=')){
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;

               }
           }
       }
       return cookieValue
   }


   const csrftoken = getCookie('csrftoken')


   const DeleteOrUpdate = () =>{
    const deleteOrCancel = [...document.getElementsByClassName('delete-cancel')]
    deleteOrCancel.forEach(form => { form.addEventListener('submit', e =>{
        e.preventDefault()
        const clickId =e.target.getAttribute('data-id')
        const btnClicked = document.getElementById(`del-cancel-${clickId}`)

        $.ajax({
            type: 'POST',
            url: '/core/delete-investment',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'pk':clickId
            },
            success:function (response){
console.log(response)
            },
            error: function (error){
console.log(error)

            }

        })
    })

    })
   }

$.ajax({
    type: 'GET',
    url:'/core/ajax-investment',
        success: function(response) {
        const data = response.data

    var remaft = 5
  countdown = data;

 

    for (var i = 0; i<countdown.length; i++ ) {
        if (checkDate(countdown[i]['timer'])){
            // wrap.innerHTML += '<tr><td id ="' + 'demos' + (i+1) + '">hi</td></tr>'
            wraps.innerHTML += `
 <tr class ='bg-pale-dark'>


                                          <td class="border-top-0">${countdown[i]['invest_id']}</td>
                                                <td class="text-center border-top-0"> ${countdown[i]['investment']}</td>
                                                <td class="text-center border-top-0"> ${countdown[i]['invested_amount'] }</td>
                                                <td class="text-center border-top-0"> ${countdown[i]['get_profit'].toFixed(2)}</td>
                                                <td class="text-center border-top-0">${countdown[i]['get_expected_return'].toFixed(2)}</td>
                                                
                                                 <td className="text-center border-top-0">${countdown[i]['status']=== 'ongoing'? 
`<div class="btn-sm btn-success btn-rounded">${countdown[i]['status']}</div>`: 
                `<div class="btn-sm btn-danger btn-rounded">${countdown[i]['status']}</div>`                                                     
}  </td>
                                                 
                                                <td class="text-center  border-top-0"> ${Date(countdown[i]['started'])}</td>
                                                <td class="text-center border-top-0 "> ${countdown[i]['duration']}day(s)</td>
                                                <td class="text-center border-top-0">${(countdown[i]['timer'])} </td>
                                                
                                                
                                                

                                                
                                                
                                                
                                                 <td class="text-center border-top-0">
                                                  <form class="delete-cancel" data-id=${countdown[i]['id']}>
                                                 ${Date.now() <=Date(countdown[i]['timer'])?
    `<button type="submit" class="btn-sm btn-outline-danger btn-round mr-sm-0" id="del-cancel-${countdown[i]['id']}" >
    <i class="fa fa-trash text-youtube margin-0 "></i>
    </button>`:
   ` <button type="submit" class="btn-sm btn-outline-warning btn-round mr-sm-0" id="del-cancel-${countdown[i]['id']}">
        <i class="fa fa-times text-yellow margin-0 "></i>
    </button>`
} 
   </form>                                               
  </td>
  
<td id="${countdown[i]['id']}" class="hellomylove">timer</td>
</tr>
`
         new MyTimers(countdown[i]['timer'], countdown[i]['id'])


        }
    }

    function checkDate(tim){
        var counter = new Date(tim).getTime()
        var now = new Date().getTime()
        var diff = counter - now

        if (diff > -60 * 1000 * remaft){
            return true
        }
        else{
            return false
        }
    }

    function MyTimers(tim, element){
        var counter = new Date(tim).getTime()
        

        var x = setInterval(function(){
            var now = new Date().getTime()
            var diff = counter - now
            const d = Math.floor(diff / (1000 * 60 * 60 * 24) )
            const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((diff % (1000 * 60)) / 1000);
            var alltime = `${d} days ${h} hours ${m} minutes ${s} seconds`



          document.getElementById(element).innerHTML = alltime
   const updateInvestmentAfterTimeout = [...document.getElementsByClassName('hellomylove')]
            updateInvestmentAfterTimeout.forEach((investment)=>{

           if (!diff===0){
               console.log('this is ',investment)
               $.ajaxSend
           }
            })




            if(diff < 0){
                if (diff > -60 * 1000 * remaft){
                    document.getElementById(element).innerHTML = 'FINISHED'
                    document.getElementById(element).classList.add("dropped-invest" )
                }
                else{
                    clearInterval(x)
                    var chekEl = document.getElementById(element)
                    if(chechEl){
chekEl.parentElement.remove()
                    }
                }

            }

      if (d ===0){
                    document.getElementById(element).classList.add("endsoon-invest" )
                }



        },1000)
         new getUpdate(tim, element)
    DeleteOrUpdate()
    }

    function getUpdate(di, element){
            var counter = new Date(di).getTime()
        var now = new Date().getTime()
        var diff = counter - now
        console.log('this is diff',diff)
                console.log('this is element',element)

    }



        },
        error : function(error){
        console.log('error', error)
        }
    })



// < td
// className = "text-center border-top-0" >
//
//     < form
// action = "{% url 'core:delete_investment' %}"
// method = "POST" >
//     { % csrf_token %
// }
// <input type="hidden" value={{amt.id}} name="id">
//
//     <button type="submit" className="btn-sm btn-outline-danger btn-round mr-sm-0"><i
//         className="fa fa-trash text-youtube margin-0 "></i></button>
//
// </form>
//
//
// </td>

            //                                                 <form action="{% url 'core:delete_investment' %}" method="POST">
         //     {% csrf_token %}
         //     <input type="hidden" value={{amt.id}} name="id">
         //
         //         <button type="submit" className="btn-sm btn-outline-danger btn-round mr-sm-0"><i className="fa fa-trash text-youtube margin-0 "></i></button>
         //
         // </form>