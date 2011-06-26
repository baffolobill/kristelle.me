function Navigation(opts){
    var settings = {
	'pageIdPrefix': 'page',
	'pageBaseClass': 'page-base',
	'spped': 800
    };

    this.settings = jQuery.extend(settings, opts);
    this.current_page = null;
    this.next_page = null;
}

Navigation.prototype = {
    arrow_left: function(obj, page_id){
	this.current_page = jQuery(obj).closest('.'+this.settings.pageBaseClass);
	this.next_page = jQuery('#'+this.settings.pageIdPrefix+page_id);

	this.animate({'direction':'left'});

	return false;
    },
    arrow_right: function(obj, page_id){
	this.current_page = jQuery(obj).closest('.'+this.settings.pageBaseClass);
	this.next_page = jQuery('#'+this.settings.pageIdPrefix+page_id);

	this.animate({'direction':'right'});

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