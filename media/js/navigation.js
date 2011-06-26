function Navigation(opts){
    var settings = {
	'pageIdPrefix': 'page',
	'pageBaseClass': 'page-base',
	'spped': 800,
	'default_page': '#page-home'
    };

    this.settings = jQuery.extend(settings, opts);
    this.current_page = null;
    this.next_page = null;
}

Navigation.prototype = {
    goto_page: function(page_id){
	if (page_id[0] != '#') page_id = '#'+page_id;

	var _p = jQuery(page_id);
	if (!(_p.length && _p.hasClass('page-base'))){
	    page_id = this.settings.default_page;
	    _p = jQuery(page_id);
	}
	jQuery('.page-base').hide();
	_p.show();
	Link.setUrlHash(page_id);
	

	return false;
    },
    arrow_left: function(obj, page_id){
	this.current_page = jQuery(obj).closest('.'+this.settings.pageBaseClass);

	this.next_page = this.current_page.prev('.'+this.settings.pageBaseClass);
	if (!this.next_page.length){
	    this.next_page = jQuery('.'+this.settings.pageBaseClass+':last');
	}

	this.animate({'direction':'left'});

	Link.setUrlHash(this.next_page.attr('id'));
	
	return false;
    },
    arrow_right: function(obj, page_id){
	this.current_page = jQuery(obj).closest('.'+this.settings.pageBaseClass);

	this.next_page = this.current_page.next('.'+this.settings.pageBaseClass);
	if (!this.next_page.length){
	    this.next_page = jQuery('.'+this.settings.pageBaseClass+':first');
	}
	
	this.animate({'direction':'right'});

	Link.setUrlHash(this.next_page.attr('id'));

	return false;
    },
    animate: function(opts){
	var self = this;

	this.current_page.hide();

	this.hide_arrows(this.next_page);
	this.next_page.show('slide', opts, self.settings.speed,
				function(){
				    self.show_arrows(self.next_page);
				});
    },
    hide_arrows: function(obj){
	obj.find('.nav-arrows,.nav-lang').hide();
    },
    show_arrows: function(obj){
	obj.find('.nav-arrows,.nav-lang').show();
    }
};
nav = new Navigation();