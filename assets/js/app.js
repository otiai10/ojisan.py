var __my_id = '';
var __unread_cnt = 0;
var __socket;

(function(){
  var Message = Backbone.Model.extend({
    defaults : {
      sender  : 'otiai10',
      content : 'おっぱい',
      sent_at : '2013-07-02 17:26:56',
    }
  });
  var Messages = Backbone.Collection.extend({model:Message});
  var MessageView = Backbone.View.extend({
    tagName  : 'li',
    template : _.template($('#message').html()),
    render   : function(){
      var tpl = this.template(this.model.toJson());
      this.$el.html(tpl);
      return this;
    },
  });
  var MessagesView = Backbone.View.extend({
    tagName : 'ul',
    render : function(){
      this.collection.each(function(m){
        var m = new MessageView({model:m});
        this.$el.append(m.render().el);
      },this);
      return this;
    },
  });

  __socket = new WebSocket("ws://oti10.com:9090/chat");
  __socket.onmessage = function(ev){
    console.log('message event => ', ev);
  } 
  __socket.onopen = function(ev){
    console.log('open event => ', ev);
    first_mess = JSON.stringify({'request':'/get/self/id','params':null});
    __socket.send(first_mess);
  }
})();
