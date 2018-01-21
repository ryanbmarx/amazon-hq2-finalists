// window.addEventListener('DOMContentLoaded', function(e){
document.querySelector('#highlight').addEventListener('change', function(e){
	const chosenBid = this.value;
	console.log(chosenBid);
	document.querySelector('[data-now-showing]').setAttribute("data-now-showing", chosenBid);
})
// })