const handleAlerts=(type, msg) =>{
    ajaxAlert.innerHTML=`
   <div class="alert alert-${type} alert-dismissible w-25 fade rounded show centered text-center" align="center" role="alert" >
   <h5><strong> ${msg}</strong></h5>
    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">
     <i class=" fas fa-trash z-index-2 text-danger"></i>
    </span></button>
    </div>
    `
}