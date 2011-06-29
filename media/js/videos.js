function Videos(opts){
    var settings = {};
    this.settings = jQuery.extend(settings, opts);
    this.container = null;
    this.vplayer = null;
}

Videos.prototype = {
    show: function(obj, video_id){
	var self = this;

	VideoJS.DOMReady(function(){
	    self.vplayer = VideoJS.setup(video_id);
	});

	jQuery.colorbox({href:'#'+video_id, 
		    inline:true,  
		    scrolling:false, 
		    innerWidth:'640px', 
		    innerHeight:'480px'});

	return false;
    }
};
videos = new Videos();
