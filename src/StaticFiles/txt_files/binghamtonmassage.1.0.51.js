var touchtime = 0;


var pathname = window.location.pathname;
var signatureArea;
$(function() {
	if (pathname === "/") {
		const pregnant = document.getElementById('yes_pregnant');
		const notPregnant = document.getElementById('not_pregnant');
		const howFarAlong = document.getElementById('how_far_along');
		const massageTypeOther = document.getElementById('massage_type_other');
		const massageTypeOtherExplain = document.getElementById('massage_type_other_text');
		const painLocationOther = document.getElementById('pain_other');
		const painLocationOtherExplain = document.getElementById('pain_type_other_text');
		const shoulderPain = document.getElementById('shoulder_pain');
		const shoulderOptions = document.getElementById('shoulder_options');
		const hipPain = document.getElementById('hip_pain');
		const hipOptions = document.getElementById('hip_options');
		const backPain = document.getElementById('back_pain');
		const backOptions = document.getElementById('back_options');
		const legPain = document.getElementById('leg_pain');
		const legOptions = document.getElementById('leg_options');
		const leftLeg = document.getElementById('leftleg_pain');
		const leftLegOptions = document.getElementById('left_leg_options');
		const rightLeg = document.getElementById('rightleg_pain');
		const rightLegOptions = document.getElementById('right_leg_options');
		const rightGlute = document.getElementById('rightglute_pain');
		const rightQuad = document.getElementById('rightquad_pain');
		const rightCalf = document.getElementById('rightcalf_pain');
		const rightHamstring = document.getElementById('righthamstring_pain');
		const leftGlute = document.getElementById('leftglute_pain');
		const leftQuad = document.getElementById('leftquad_pain');
		const leftCalf = document.getElementById('leftcalf_pain');
		const leftHamstring = document.getElementById('lefthamstring_pain');
		const leftHip = document.getElementById('lefthip_pain');
		const rightHip = document.getElementById('righthip_pain');
		const leftShoulder = document.getElementById('leftshoulder_pain');
		const rightShoulder = document.getElementById('rightshoulder_pain');
		const upperBack = document.getElementById('upperback_pain');
		const lowerBack = document.getElementById('lowerback_pain');
		const intakeForm = document.getElementById('intakeForm');
		const resetSignature = document.getElementById("reset_signature");
		try {
			intakeForm.addEventListener("submit", moveSignatureData);
			
			const inputs = document.querySelectorAll('input');
			inputs.forEach(input => {
			  	input.setAttribute('autocomplete', 'off');
			});
			
			window.addEventListener("pageshow", () => {
			  	const form = document.querySelector('form');
			    if (form) {
			    	form.reset();
			    }
			    resetSignaturePad();
			});
			
			resetSignature.addEventListener('click', function(){
				resetSignaturePad();
			});
			
			shoulderPain.addEventListener('change', function() {
				if (shoulderPain.checked) {
					shoulderOptions.style.display = 'block';
				} else {
					shoulderOptions.style.display = 'none';
					rightShoulder.checked = false;
					leftShoulder.checked = false;
				}
			});
			
			hipPain.addEventListener('change', function() {
				if (hipPain.checked) {
					hipOptions.style.display = 'block';
				} else {
					hipOptions.style.display = 'none';
					rightHip.checked = false;
					leftHip.checked = false;
				}
			});
			
			backPain.addEventListener('change', function() {
				if (backPain.checked) {
					backOptions.style.display = 'block';
				} else {
					backOptions.style.display = 'none';
					lowerBack.checked = false;
					upperBack.checked = false;
				}
			});
			
			legPain.addEventListener('change', function() {
				if (legPain.checked) {
					legOptions.style.display = 'block';
				} else {
					legOptions.style.display = 'none';
					rightCalf.checked = false;
					rightQuad.checked = false;
					rightHamstring.checked = false;
					rightGlute.checked = false;
					rightLeg.checked = false;
					leftCalf.checked = false;
					leftQuad.checked = false;
					leftHamstring.checked = false;
					leftGlute.checked = false;
					leftLeg.checked = false;
				}
			});
			
			leftLeg.addEventListener('change', function() {
				if (leftLeg.checked) {
					leftLegOptions.style.display = 'block';
				} else {
					leftLegOptions.style.display = 'none';
					leftCalf.checked = false;
					leftQuad.checked = false;
					leftHamstring.checked = false;
					leftGlute.checked = false;
				}
			});
			
			rightLeg.addEventListener('change', function() {
				if (rightLeg.checked) {
					rightLegOptions.style.display = 'block';
				} else {
					rightLegOptions.style.display = 'none';
					rightCalf.checked = false;
					rightQuad.checked = false;
					rightHamstring.checked = false;
					rightGlute.checked = false;
				}
			});
			
			painLocationOther.addEventListener('change', function() {
				if (painLocationOther.checked) {
					painLocationOtherExplain.style.display = 'block';
				} else {
					painLocationOtherExplain.style.display = 'none';
				}
			});
			
			massageTypeOther.addEventListener('change', function() {
				if (massageTypeOther.checked) {
					massageTypeOtherExplain.style.display = 'block';
				} else {
					massageTypeOtherExplain.style.display = 'none';
				}
			});
			
			pregnant.addEventListener('change', function() {
			    if (pregnant.checked) {
			        howFarAlong.style.display = 'block';
			    }
			});
			
			notPregnant.addEventListener('change', function() {
			    if (notPregnant.checked) {
			        howFarAlong.style.display = 'none';
			    }
			});
			
			// This is the part where jSignature is initialized.
			signatureArea = $("#signature").jSignature({'UndoButton':false});
			
		} catch(error) {
			console.error(error);
		}
	}
	if (pathname === "/save") {
		try {
			$("#logo_img_reset").on("click", function() {
			    if (touchtime === 0) {
			        // set first click
			        touchtime = Date.now();
			    } else {
			        if (((Date.now()) - touchtime) < 800) {
			            location.href = "/";
			            touchtime = 0;
			        } else {
			            // not a double click so set as a new first click
			            touchtime = Date.now();
			        }
			    }
			});
		} catch(error) {
			console.error(error);
		}
	}
	
	if (pathname === "/hidden") {
		try {
			$("#logo_img_reset").on("click", function() {
			    if (touchtime === 0) {
			        // set first click
			        touchtime = Date.now();
			    } else {
			        if (((Date.now()) - touchtime) < 800) {
			            location.href = "/clientList";
			            touchtime = 0;
			        } else {
			            // not a double click so set as a new first click
			            touchtime = Date.now();
			        }
			    }
			});
		} catch(error) {
			console.error(error);
		}
	}

	if (pathname === "/clientList") {
		try {
			$("#search").keyup(function(event) {
				//if (event.keyCode === 13) {
					searchTable();
				//}
			});
		} catch(error) {
			console.error(error);
		}
		
		$("#search_button").click(function() {
			searchTable();
		});
		
		$("#clear_button").click(function(){
			$("#search").val("");
			searchTableForString("");
		});
		
		initializeTable();
	}
	
	if (pathname === "/clientData") {
		$("#hide_button").click(function() {
			location.href = "/hidden";
		})
	}
});

function resetSignaturePad(){
	try {
		signatureArea.jSignature('reset');
	} catch(error) {
		console.error(error);
	}
}

function initializeTable(){
    try {
		var i;
		var rows =  document.getElementsByClassName("tableRow");
		for (i=0; i<rows.length; i+=1) {
			rows[i].addEventListener('click', function(event){
				gotoRow(event.target.parentElement.id);
			});
		}
	} catch(error) {
		console.error(error);
	}
}


function moveSignatureData(){
	var success = false;
	var data = $("#signature").jSignature("getData", "svg");
	if (data.length === 2) {
		$("#signature_data").val(data[1]);
		if (getInnerSvg(data[1]) !== "") {
			success = true;
		}
	}
	return success;
}



function getInnerSvg(xmlString) {
	var textData = "";
	try {
		const parser = new DOMParser();
		const xmlDoc = parser.parseFromString(xmlString, "text/xml");
		const svgNodes = xmlDoc.getElementsByTagName("svg");
	    const imageData = svgNodes[0];
	    const path = imageData.getElementsByTagName("path");
	    if (path) {
			textData = path[0].getAttribute("d");
		}
    } catch (error){
		console.error("error decoding signature", error.message);
	}
    return textData;
}


function gotoRow(row_id) {
	location.href  = '/clientData?tid=' + row_id;
}

function searchTable() {
	searchTableForString(document.getElementById("search"));
}

function searchTableForString(input) {
	var input;
	var filter = "";
	var table;
	var tr;
	var td0; 
	var td1;
	var i;
	var txtValue0;
	var txtValue1;
	if (input !== "") {
		filter = input.value.toUpperCase();
	} 
	table = document.getElementById("userTable");
	tr = table.getElementsByTagName("tr");
	$("tr").removeClass("boldTop");
	for (i = 0; i < tr.length; i+=1) {
		td0 = tr[i].getElementsByTagName("td")[0];
		td1 = tr[i].getElementsByTagName("td")[1];
		if (td0 && td1) {
			txtValue0 = td0.textContent || td0.innerText;
			txtValue1 = td1.textContent || td1.innerText;
			if ((txtValue0.toUpperCase().indexOf(filter) > -1) || (txtValue1.toUpperCase().indexOf(filter) > -1)) {
			    tr[i].style.display = "";
			} else {
			    tr[i].style.display = "none";
			}
		}
	}
}

function sortTable(columnIndex) {
    const table = document.getElementById("userTable");
    const tbody = document.getElementById("tableBody");
    const rows = Array.from(tbody.rows);
    const currentSortColumn = table.querySelector("th.sort-asc") || table.querySelector("th.sort-desc");
    const isAscending = currentSortColumn === null || !currentSortColumn.classList.contains("sort-asc");

	$("tr").removeClass("boldTop");
    // Remove sorting indicators from all headers
    table.querySelectorAll("th").forEach(th => {
        th.classList.remove("sort-asc", "sort-desc");
    });

    rows.sort((rowA, rowB) => {
        const cellA = rowA.cells[columnIndex].textContent.toLowerCase();
        const cellB = rowB.cells[columnIndex].textContent.toLowerCase();

        if (columnIndex === 2) { // Sort by date
            const dateA = new Date(cellA);
            const dateB = new Date(cellB);
            return isAscending ? dateA - dateB : dateB - dateA;
        } else { // Sort alphabetically
            return isAscending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
        }
    });

    // Add the appropriate sorting class to the clicked header
    const header = table.querySelector(`th:nth-child(${columnIndex + 1})`);
    header.classList.add(isAscending ? "sort-asc" : "sort-desc");

    // Append the sorted rows back to the tbody
    rows.forEach(row => tbody.appendChild(row));
}

function signOut() {
	setCookie("gstatBMaW", "", 0);
	setCookie("g_state", "", 0);
	setCookie("g_csrf_token", "", 0);
    location.href = "/signout";
}

function setCookie(cookieName, cookieValue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	let expires = "expires="+ d.toUTCString();
	document.cookie = cookieName + "=" + cookieValue + "; expires=" + expires + "; path=/; secure; samesite=strict";
}
