function Photos(opts){
    var settings = {
	'blockId': '.page__wrapper.photos',
	'speed': 700
    };
    this.settings = jQuery.extend(settings, opts);
    this.album_id = null;
    this.container = null;
    this.cache_container = null;
    this.album_photos_page = null;
}

Photos.prototype = {
    back: function(){
	this.album_photos_page.hide();
	this.album_photos_page = null;
	this.animate(this.container, {'direction':'left'});

	return false;
    },
    popup: function(obj, album_id){
	var self = this;
	var url = jQuery(obj).attr('href');
	var album_group = 'group'+album_id;

	jQuery.colorbox({href:url, rel:album_group});

	return false;
    },
    get_album_photos: function(obj, album_id){
	var self = this;
	var url = jQuery(obj).attr('href').substr(1);
	this.album_id = album_id;
	this.container = jQuery('#album-photos');
	this.cache_container = jQuery('#album-photos-block');

	if (!this.is_cached()){
	    this.block();
	    jQuery.get(url, {'ajax':1},
		       function(data){
			   self.unblock();
			   if (data.error){
			       // show error
			       messenger.error(data.error);
			   } else if (data.html){
			       self.cache_and_show(data.html);
			   }
		       }, 'json');
	} else {
	    this.album_photos_page = this.get_cache(this.album_id);
	    
	    this.container.hide();
	    this.animate(this.album_photos_page, {'direction':'right'});
	}

	return false;
    },
    block: function(){
	jQuery(this.settings.blockId).block({
		message: null,
		fadeIn:0,
		fadeOut:0,
		overlayCSS:{backgroundColor:'#fff'}
	    });
	jQuery('.page__wrapper.photos>.context-loader').show();
    },
    unblock: function(){
	jQuery('.page__wrapper.photos>.context-loader').hide();

	jQuery(this.settings.blockId).unblock();
    },
    cache_and_show: function(html){
	if (!this.is_cached()){
	    this.cache(html);
	}

	this.album_photos_page = this.get_cache(this.album_id);

	this.container.hide();
	this.animate(this.album_photos_page, {'direction':'right'});
    },
    animate: function(obj, opts){
	var self = this;

	obj.show('slide', opts, self.settings.speed);
    },
    is_cached: function(){
	var _c = this.cache_container.children('#album-photos-'+this.album_id);
	if (_c.length)
	    return true;
	else
	    return false;
    },
    cache: function(html){
	var _c = jQuery('<div id="album-photos-'+this.album_id+'" class="album-photos-cache-block clearfix" style="display:none;"></div>').html(html);
	this.cache_container.append(_c);
	this.bind(_c);
    },
    bind: function(container){
	jQuery('a.album__image__button', container).colorbox({'rel':'group'+this.album_id});
    },
    get_cache: function(album_id){
	return this.cache_container.children('#album-photos-'+album_id);
    }
};
photos = new Photos();
