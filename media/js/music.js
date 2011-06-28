function Music(opts){
    var settings = {
	jplayerId: '#player-block'
    };
    this.settings = jQuery.extend(settings, opts);
    this.current_track = null;
    this.current_track_id = null;
    this.track_meta = null;
    this.player = jQuery(this.settings.jplayerId);

}

Music.prototype = {
    getTrack: function(obj){
	this.current_track = jQuery(obj).closest('.music-track');
	this.track_meta = this.current_track.find('.track__meta');
    },
    play_next_or_stop: function(event){
	var _class = '';
	if (this.current_track.hasClass('music-single-track')){
	    _class = '.music-single-track';
	} else if (this.current_track.hasClass('tracklist__track')){
	    _class = '.tracklist__track';
	}

	if (_class != ''){
	    var next = this.current_track.next(_class);
	    if (next.length){

		this.current_track = next;
		this.track_meta = this.current_track.find('.track__meta');
		this._play();
		return;
	    }
	}
	this.current_track.removeClass('active');
	this.current_track = null;
	this.track_meta = null;
	this.current_track_id = null;
    },
    play: function(obj){
	this.getTrack(obj);
	this._play();
    },
    _play: function(){
	var self = this;

	jQuery('.music-track.active').removeClass('active');
	this.current_track.addClass('active');
	if (this.current_track_id != this.getTrackId()){
	    this.current_track_id = this.getTrackId();
	    this.player.jPlayer('setMedia', {
		    'mp3':self.getTrackFile(),
		    'name':self.getTrackName()
		    });
	}
	this.player.jPlayer('play');
    },
    stop: function(obj){
	this.pause(obj);
    },
    pause: function(obj){
	this.current_track.removeClass('active');
	this.player.jPlayer('pause');
    },
    getTrackName: function(){
	return this.track_meta.children('.track__meta__name').html();
    },
    getTrackFile: function(){
	return this.track_meta.children('.track__meta__file').html();
    },
    getTrackId: function(){
	return this.track_meta.children('.track__meta__id').html();
    }
};
music = new Music();

jQuery(document).ready(function($){
  $('.music-track').hover(function(){
    $(this).addClass('hover');
  },function(){
    $(this).removeClass('hover');
  });

  $('.music-track>.track__play,.music-track>.track__title').click(function(e){
    if ($(this).parent().hasClass('active')){
      music.stop(this);
    } else {
      music.play(this);
    }
    return false;
  });

});
