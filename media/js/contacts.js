function Contacts(){
    this.settings = {
	'blockId': '.page__wrapper.contacts'
    };
}
Contacts.prototype = {
    send: function(obj){
	var self = this;
	var form = jQuery(obj).closest('form');
	var data = form.serialize();

	this.block();
	jQuery.post(form.attr('action'), data,
		    function(response){
			//jQuery(obj).show();
			self.unblock();
			if (response.error){
			    messenger.error(response.error);
			} else if (response.message){
			    messenger.notify(response.message);
			} else {
			    self.clear(form);
			}
		    }, 'json');
	jQuery(obj).show();
	return false;
    },
    clear: function(form){
	form.find('textarea').val('');
    },

    block: function(){
	jQuery(this.settings.blockId).block({
		message: null,
		fadeIn:0,
		fadeOut:0,
		overlayCSS:{backgroundColor:'#fff'}
	    });
	jQuery('.page__wrapper.contacts>.context-loader').show();
    },
    unblock: function(){
	jQuery('.page__wrapper.contacts>.context-loader').hide();

	jQuery(this.settings.blockId).unblock();
    }
};
var contacts = new Contacts();
