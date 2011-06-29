function Videos(opts){
    var settings = {};
    this.settings = jQuery.extend(settings, opts);
    this.container = null;
}

Videos.prototype = {
    show: function(obj, src){
	var self = this;

	jQuery('#video-player').jPlayer('setMedia', {
		'm4v': src
	    });
	jQuery.colorbox({href:'#video-player-block', inline:true});

	return false;
    }
};
videos = new Videos();
