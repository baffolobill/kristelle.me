function Contacts(){

}
Contacts.prototype = {
    send: function(obj){
	var self = this;
	var form = jQuery(obj).closest('form');
	var data = form.serialize();

	jQuery(obj).hide();

	jQuery.post(form.attr('action'), data,
		    function(response){
			//jQuery(obj).show();
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
    }
};
var contacts = new Contacts();
