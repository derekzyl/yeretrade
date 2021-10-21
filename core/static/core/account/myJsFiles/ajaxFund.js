const amount = document.getElementById('id_amount_to_fund')
const button = document.getElementById('fund_button')
const type = document.getElementById('id_type')
const fundForm = document.getElementById('theFundForm')
const ajaxAlert= document.getElementById('ajax-alert')
const ModalForm= document.getElementById('modal-form')
const DepositAlert= document.getElementById('deposit-alert')
const Proceed= document.getElementById('continue-deposit')
const zone= document.getElementById('my-dropzone')





const csrf = document.getElementsByName('csrfmiddlewaretoken')




fundForm.addEventListener('change',()=>{

     amount.value===0?button.classList.add('disabled'):(button.classList.remove('disabled , btn-light'))




}
)
console.log(ajaxAlert.value)

const handleAlerts=(type, msg) =>{
    ajaxAlert.innerHTML=`
   <div class="alert alert-${type} alert-dismissible  fade rounded show " align="center" style=" position:relative;" role="alert" >
   <h5><strong> ${msg}</strong></h5>
    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">
     <i class=" fas fa-trash z-index-2 text-danger"></i>
    </span></button>
    </div>
    `
}

fundForm.addEventListener('submit', e =>{
    e.preventDefault();
    console.log(type.value, amount.value)
    if(amount.value!==0 && amount.value> 0 ){
           $.ajax(
        {
            type: 'POST',
            url:'/core/fund-account',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'amount_to_fund':amount.value,
                'type':type.value
            },
            success: function(response){

//                                 handleAlerts('success', `proceed to deposit $${response.amount} worth of ${response.type}
//
// then submit evidence of payment`)

                    DepositAlert.innerHTML =`
   <div class="alert alert-success alert-dismissible  fade rounded show " align="center" style=" position:relative;" role="alert" >
   <h5><strong>proceed to deposit $${response.amount} worth of ${response.type}
then submit evidence of payment</strong></h5>
    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">
     <i class=" fas fa-trash z-index-2 text-danger"></i>
    </span></button>
    </div>
    `

                button.classList.add('deposit-see')
                fundForm.classList.add('deposit-see')
                Proceed.classList.remove('deposit-see')


                                // window.location.href = (response.url)

//                 if (response.succeed){
//                     ModalForm.innerHTML = `<div class="spinner-border text-success" role="status">
// <span class="sr-only">Loading...</span>
// </div>`
//                 }


            },
            error: function (error) {
                               handleAlerts('danger', `${error}`)


            }

        }
    )
    }
    else{        $('#exampleModal').modal('hide')
        handleAlerts('warning', 'input amount')}


}
)


Dropzone.autoDiscover = false
let myDropzone = new Dropzone('#my-dropzone',{
    url : 'comfirm-payment',

    maxFiles:1,
    maxFilesize:1,
    acceptedFiles: '.jpeg, .png, .jpg'
})

console.log(myDropzone)

// const xm = Dropzone.options.myDropzone ={
//     paramName: 'file',
//     maxFilesize: 1,
//     maxFiles: 1,
//
// }
// console.log(xm)
