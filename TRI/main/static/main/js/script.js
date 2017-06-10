$(function () {
    $("#mynav").append($("#mainNav").clone().attr("id", "mynav").attr("class", ""));
    $("#mynav").mmenu({
        "extensions" : [
			"effect-menu-zoom",
			"effect-panels-zoom",
			"pagedim-black"
		],
		"offCanvas" :{
			"position" : "right"
		},
		"navbar" :{
			"title" : "TRI Organization"
		}
    });
});

$(document).ready(function() {
    $("#team").owlCarousel({
        singleItem:true,
        pagination:false,
        navigation:true,
        navigationText:["",""],
        slideSpeed: 800,
        paginationSpeed: 800
    });
});
