

     const referMain = document.getElementById('ajax-main')
          const referInvest = document.getElementById('ajax-invest')


    $.ajax({
    type: 'GET',
    url:'/core/ajax-referral',
        success: function(response) {

            const data = response.data

            data.forEach(el =>{
                el.the_main.forEach(ele=>{
                           // refer.innerHTML +=ele.user

                         referMain.innerHTML +=` <td class="text-center border-top-0 text-white">${ele.user} </td>
<td class="text-center border-top-0 text-success"  >${ele.main_balance} </td>
<td class="text-center border-top-0 text-google">${ele.main_earning} </td>`

                })

el.the_invest.forEach(ele =>{
    var i = 1
   i <=ele.length


    referInvest.innerHTML +=`
<!--                                                <td class="text-center border-top-0 text-info">${i++}</td>-->
                                                <td class="text-center border-top-0 text-info">${ele.invest_id}</td>
                                                <td class="text-center border-top-0 text-info">${ele.invest_user}</td>
                                                <td class="text-center border-top-0 text-yellow">${ele.invest_name} PLAN</td>
                                                <td class="text-center border-top-0 text-google">${ele.invest_amount}</td>
                                                <td class="text-center border-top-0 text-primary"> ${ele.invest_return}</td>
                                                <td class="text-center border-top-0 text-info">${ new Date(ele.invest_timer)}</td>
                                                

`

})

            })
        },
        error : function(error){
        console.log('error', error)
        }
    })
















    // < tr
    //  className = "bg-pale-dark" >
    //      < td
    //  className = "border-top-0" > {
    //  {
    //      forloop.counter
    //  }
    //  } </td>
    //  <td className="text-center border-top-0">
    //  {
    //      {
    //          amt.investment
    //      }
    //  }
    //  </td>
    //  <td className="text-center border-top-0">
    //  {
    //      {
    //          amt.invested_amount
    //      }
    //  }
    //  </td>
    //  <td className="text-center border-top-0">
    //  {
    //      {
    //          amt.get_profit | floatformat
    //      :
    //          2
    //      }
    //  }
    //  </td>
    //  <td className="text-center border-top-0">
    //  {
    //      {
    //          amt.get_expected_return | floatformat
    //      :
    //          2
    //      }
    //  }
    //  </td>
    //
    //  <td className="text-center border-top-0">
    //  {%
    //      if amt.status == 'ongoing' %}
    //  <span className="btn-sm btn-success btn-rounded">{{amt.status}}</span>
    //
    //  {% else %
    //  }
    //  <span className="btn-sm btn-danger btn-rounded">{{amt.status}}</span>
    //  {%
    //      endif %
    //  }
    //  </td>
    //
    //  <td className="text-center  border-top-0">
    //  {
    //      {
    //          amt.started
    //      }
    //  }
    //  </td>
    //  <td className="text-center border-top-0 ">
    //  {
    //      {
    //          amt.duration
    //      }
    //  }
    //  day(s) < /td>
    //  <td className="text-center border-top-0">{{amt.timer}} </td>
    //  <td className="text-center border-top-0">
    //      <form action="{% url 'core:delete_investment' %}" method="POST">
    //          {% csrf_token %}
    //          <input type="hidden" value={{amt.id}} name="id">
    //
    //              <button type="submit" className="btn-sm btn-outline-danger btn-round mr-sm-0"><i
    //                  className="fa fa-trash text-youtube margin-0 "></i></button>
    //
    //      </form>
    //
    //
    //  </td>
    //
    //
    //  </tr>
