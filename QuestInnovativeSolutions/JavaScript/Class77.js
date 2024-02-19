function datasubmit()
{
    var nm=document.getElementById("name")
    var pa=document.getElementById("password")
    if (nm.value==''||pa.value=='')
    {
        alert('No blank values allowed')
        return false
    }
    else
    {
        alert("Success")
        return true
    }
}