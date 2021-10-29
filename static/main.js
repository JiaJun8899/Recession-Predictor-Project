$(document).ready(function(){
    console.log("Ready!");
    addevent();
});
function addevent()
{
    var chk = document.getElementById("graph");
    chk.addEventListener("click",print_selected);
}
function print_selected(e)
{
    var pop = document.getElementById("options");
    var chk = document.getElementById("graph");
    var strUser = chk.value;
    chk.addEventListener("click",print_selected);
    if (pop === null && strUser === 'multiple'){
        document.getElementById("date_filter").style.display="inline";
        pop = document.createElement("div");
        pop.id = 'options';
        pop.class = 'col-sm';
        pop.innerHTML= '<input type="checkbox" id="cpi" value="CPI" name="chk"><label for="cpi">Consumer Price index</label><br>';
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="recession" value="Recession" name="chk"><label for="recession">Recession</label><br>'
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="unemploy" value="Unemployment Rate" name="chk"><label for="unemploy">Unemployment Rate</label><br>'
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="market_yield" value="Market Yield" name="chk"><label for="market_yield">Market Yield</label><br>'
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="industrial" value="Industrial Production Rate" name="chk"><label for="industrial">Industrial Production Rate</label><br>'
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="treasury" value="Treasury Bill Rate" name="chk"><label for="treasury">Treasury Bill Rate</label><br>'
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="capacity" value="Capacity Utilization" name="chk"><label for="capacity">Capacity Utilization</label><br>'
        pop.innerHTML = pop.innerHTML + '<input type="checkbox" id="diff" value="diff" name="diff"><label for="diff">Difference</label>'
        e.target.insertAdjacentElement("afterend", pop);
    }
    else{
        pop.remove();
        document.getElementById("date_filter").style.display="none";
    }
}
