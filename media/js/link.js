function LinkObject(){
    this.settings = {};
}
LinkObject.prototype = {
    
    getCurrentUrl: function(){
        var _url = window.location;

        return _url.pathname+_url.search+_url.hash;
    },

    setUrlAsCurrent: function(url){
        window.location.href = url;

        return true;
    },

    setUrlHashForUrl: function(url, value){
        var _url = url;
        var _url_wo_hash = _url.substr(0, _url.lastIndexOf('#'));
        var new_url = _url_wo_hash;

        if (value.indexOf('#')!=0)
            new_url += '#';
            
        new_url += value;

        return new_url;
    },

    setUrlHash: function(value){
        return this.setUrlAsCurrent(this.setUrlHashForUrl(this.getCurrentUrl(),
                                                            value));
    },

    getHashFromUrl: function(url){
        if (url.indexOf('#')==-1)
            return '';
        
        return url.substr(url.indexOf('#'));    
    },
    
    getHashFromCurrentUrl: function(){
        return this.getHashFromUrl(this.getCurrentUrl());
    },
    
    getPathnameFromHash: function(hash, default_value){
        if (hash.length==0)
            return default_value;
            
        var _pathname = hash.substr(hash.indexOf('#')+1);
        
        if (_pathname.length==0)
            return default_value;
            
        return _pathname;
    },    
    
    getPathnameFromHashOfCurrentUrl: function(default_value){
        return this.getPathnameFromHash(this.getHashFromCurrentUrl(), default_value);
    }    
};
var Link = new LinkObject();