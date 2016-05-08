
/* Script di controllo preventivo dei campi del login */

function checkLogin(){
		var username = document.loginForm.username.value;
		var password = document.loginForm.password.value;
		var uok=true;
		var pok=true;

		if ((username == "") || (username == "undefined")){
			document.getElementById('userError').innerHTML = '<p class="errore">(!) Username non valido</p>';
			uok=false;
		}
		else{
			document.getElementById('userError').innerHTML = '';
			uok=true;
		}
		if ((password == "") || (password == "undefined")){
			document.getElementById('passError').innerHTML = '<p class="errore">(!) Password non valida</p>';
			pok=false;
		}
		else{
			document.getElementById('passError').innerHTML = '';
			pok=true;
		}

		return (uok && pok);
	}
/* FINE */

$(document).ready(function(){

	$("#sezione-nav-1").click(function(){
		var presente=$("#panel-nav-1").css("display");
		if (presente=="none"){
			$("#panel-nav-1").css("display","block");
		}else{
			$("#panel-nav-1").css("display","");
		}

	});
});

/* SCRIPT PER LA GESTIONE RESPONSIVE DEL MENU', DEI LINK ESTERNI E DEI DOCUMENTI/ARTICOLI */

$(document).ready(function(){

	$("#sezione-sidebar").click(function(){
		var presente=$("#panel-sidebar").css("display");
		if (presente=="none"){
			$("#panel-sidebar").css("display","block");
		}else{
			$("#panel-sidebar").css("display","");
		}

	});
});

$(document).ready(function(){

	$(".sezione").click(function(){
		/* $(this).hide(); */
		var id=$(this).attr('id'); // mi salvo l'id dell'articolo su cui clicco
		var parent = $(this).parent("div"); // .attr('id'); // closest // risalgo al padre dell'elemento su cui abbiamo fatto il click
		var son = parent.find(".nascondi-articolo");

		var attr = son.attr('id');
		// alert(attr);

		if (attr === undefined) {
			son.attr('id','mostra');
		}else{
			// alert('attributo esiste');
			son.removeAttr("id");
		}

		var attr = son.attr('id');
		// alert(attr);

	});
});

/* FINE */

/* GESTIONE SIDEBAR POSIZIONAMENTO */ /* DA NON FARE SE USA IE6 */
function msieversion()
   {
      var ua = window.navigator.userAgent;
      var msie = ua.indexOf ( "MSIE " );

      if ( msie > 0 )      // If Internet Explorer, return version number
         return parseInt (ua.substring (msie+5, ua.indexOf (".", msie )));
      else                 // If another browser, return 0
         return 11;
}



var ie = msieversion();
if (ie >= 9){
	$(document).ready(function(){

		var topFixed=320;
		if ($(window).width() > 850){
				// mi salavo di quanto la scroll è distante dall'inizio pagina
				var y = $(window).scrollTop();

				if (y >= topFixed){ // se è maggiore di un valore fissato devo cambiarli classe e metterla fissa (GESTIONE RELOAD PAGINA GIA' SCROLLATA)
					$("#sidebar").addClass("sidebar-fixed");
					$("#sidebar").attr("id","sidebarFix");
				}

		}
	});

	// scroll
	$(window).scroll(function(){

			if($(window).width() > 850){

				var topFixed=320;
				// alert(topFixed);
				var y = $(window).scrollTop();
				// alert(y);
				if (y>= topFixed){
						// alert("maggiore");
						$("#sidebar").addClass("sidebar-fixed");
						$("#sidebar").attr("id","sidebarFix");
				}else{
						$("#sidebarFix").removeClass("sidebar-fixed");
						$("#sidebarFix").attr("id","sidebar");
				}
			}else{}
	});


	// resize
	$(window).resize(function(){

		if($(window).width() > 850){
				var topFixed=320;
				var y = $(window).scrollTop();

				if (y >= topFixed){ // se è maggiore di un valore fissato devo cambiarli classe e metterla fissa (GESTIONE RELOAD PAGINA GIA' SCROLLATA)
					$("#sidebar").addClass("sidebar-fixed");
					$("#sidebar").attr("id","sidebarFix");
				}
		}
		else{
			// se siamo nella parte mobile/tablet
				$("#sidebarFix").removeClass("sidebar-fixed");
				$("#sidebarFix").attr("id","sidebar");
		}

	});

}
/* FINE */

/* SCRIPT PER IL BOX TORNA SU */

$(function() {
	  $(window).scroll(function() {
	       if($(this).scrollTop() > 0) {
	            //se non siamo in cima alla pagina
	            $('#boxTop').fadeIn(); //faccio apparire il box
	        } else {
	            //altrimenti (il visitatore è in cima alla pagina scrollTop = 0)
	            $('#boxTop').fadeOut();//Il box scompare
	        }
	    });//Allo scroll function

	    $('#boxTop').click(function() {
	                //Se clicco sul box torno su (scrollTop:0) con un timing di animazione.
	        $('body,html').animate({scrollTop:0},800);
	    });//Click

});//DOM

/* FINE */



/* SCRIPT PER LA PREVALIDAZIONE DEI FORM DI INSERIMENTO */

function checkInserimentoArticolo(){
	var luogo = document.inserisciArticoloForm.luogo.value;
	var datepicker = document.inserisciArticoloForm.datepicker.value;
	var titolo = document.inserisciArticoloForm.titolo.value;
	var testo = document.inserisciArticoloForm.testo.value;
	var foto = document.inserisciArticoloForm.foto.value;
	var altfoto = document.inserisciArticoloForm.altfoto.value;
	var lok = true;
	var dok = true;
	var tok = true;
	var teok = true;
	var fok = true;
	var aok = true;

	document.getElementById('errors').innerHTML = " ";

	if ((luogo == "") || (luogo == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Luogo non valido</p>';
			lok=false;
		}

	if ((datepicker == "") || (datepicker == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Data non valida</p>';
			dok=false;
		}

	if ((titolo == "") || (titolo == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Titolo non valido</p>';
			tok=false;
		}

	if ((testo == "") || (testo == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Testo non valido</p>';
			teok=false;
		}

	if(foto){
		if ((altfoto == "") || (altfoto == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Descrizione fotografia non valida</p>';
			aok=false;
		}
	}

	return (lok && dok && tok && teok && aok);
}

function checkInserimentoDocumento(){
	var titolo = document.inserisciDocumentoForm.titolo.value;
	var testo = document.inserisciDocumentoForm.testo.value;
	var doc = document.inserisciDocumentoForm.documento.value;
	var tok = true;
	var teok = true;
	var dok = true;

	document.getElementById('errors').innerHTML = " ";

	if ((titolo == "") || (titolo == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Titolo non valido</p>';
			tok=false;
		}

	if ((testo == "") || (testo == "undefined")){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Testo non valido</p>';
			teok=false;
		}

	if (!(doc)){
			document.getElementById('errors').innerHTML += '<p class="errore"> (!) Nessun documento inserito</p>';
			doc=false;
		}

	return (tok && teok && dok);
}

/* FINE */


/* CAMBIO DI SELECT VALUE*/

function selectChange(){
	document.selectCategory.submit();
}

/* FINE */

/* SCRIPT RIPOSIZIONAMENTO ULTIMI ARTICOLI VISUALIZZATI */

function scrollTo(){
	location.hash = "#anchor";
}

/* FINE */


/* SCRIPT PER LA GESTIONE DELL'EDITOR DELL'AREA RISERVATA */

var idTextArea;

function setId(idValue){
	idTextArea=idValue;
}

function InsertCodeInTextArea(textValue) {
       //Get textArea HTML control
       var txtArea = document.getElementById(idTextArea);

       //IE
       if (document.selection) {
	         txtArea.focus();
	         var sel = document.selection.createRange();
	         sel.text = textValue;
		     return;
		}
		//Firefox, chrome, mozilla
		else if (txtArea.selectionStart || txtArea.selectionStart == '0') {
		         var startPos = txtArea.selectionStart;
		         var endPos = txtArea.selectionEnd;
		         var scrollTop = txtArea.scrollTop;
		         txtArea.value = txtArea.value.substring(0, startPos) + textValue + txtArea.value.substring(endPos, txtArea.value.length);
		         txtArea.focus();
		         txtArea.selectionStart = startPos + textValue.length;
		         txtArea.selectionEnd = startPos + textValue.length;
		      }
		      else {
		         txtArea.value += textArea.value;
		         txtArea.focus();
		      }
}

$(function() {
	$("#datepicker").datepicker({
		dateFormat: "yy/mm/dd",
		onSelect: function(dateText, inst) {
			var date = $.datepicker.parseDate(inst.settings.dateFormat || $.datepicker._defaults.dateFormat, dateText, inst.settings);
			var dateText1 = $.datepicker.formatDate("D, d M yy", date, inst.settings);
			date.setDate(date.getDate() + 7);
			var dateText2 = $.datepicker.formatDate("D, d M yy", date, inst.settings);
		}
	});
});


/* FINE */





