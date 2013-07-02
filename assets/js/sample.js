(function(){
  // Backbone
  var Task = Backbone.Model.extend({
    defaults: {
      title : 'do something',
      completed : false,
    },
    validate : function(attrs){
      if(_.isEmpty(attrs.title)){
        return 'Title must not be empty';
      }
    },
    initialize : function(){
      this.on('invalid',function(model,error){
        $('#error').html(error);
      });
    },
  });
  var Tasks = Backbone.Collection.extend({model:Task});

  var TaskView = Backbone.View.extend({
    tagName : 'li',
    initialize : function(){
      this.model.on('destroy',this.remove, this);
      this.model.on('change',this.render, this);
    },
    events  : {
      'click .delete' : 'destroy',
      'click .toggle' : 'toggle'
    },
    toggle : function(){
      this.model.set('completed', !this.model.get('completed'));
    },
    destroy : function(){
      if(confirm('are you sure?')){
        this.model.destroy();
      }
    },
    remove : function(){
      this.$el.remove();
    },
    template: _.template($('#task-template').html()),
    render : function(){
      var tpl = this.template(this.model.toJSON());
      this.$el.html(tpl);
      return this;
    }
  });
  var TasksView = Backbone.View.extend({
    tagName : 'ul',
    initialize : function(){
      this.collection.on('add', this.addNew, this);
      this.collection.on('change', this.updateCount, this);
      this.collection.on('destroy', this.updateCount, this);
    },
    addNew : function(task){
      var taskView = new TaskView({model:task});
      this.$el.append(taskView.render().el);
      this.updateCount();
      $('#title').val('').focus();
      return this;
    },
    updateCount : function(){
      var uncompletedTaskes = this.collection.filter(function(task){
        return !task.get('completed');
      });
      $('#count').html(uncompletedTaskes.length);
    },
    render : function(){
      this.collection.each(function(task){
        var taskView = new TaskView({model:task});
        this.$el.append(taskView.render().el);
      },this);
      this.updateCount();
      return this;
    }
  });

  var AddTaskView = Backbone.View.extend({
    el : '#addTask',
    events : {
      'submit' : 'submit'
    },
    submit : function(e){
      e.preventDefault();
      //var task = new Task({title: $('#title').val()});
      var task = new Task();
      if (task.set({title:$('#title').val()}, {validate : true})) {
        this.collection.add(task);
        $('#error').empty();
      }
    },
  });
  var tasks = new Tasks([
    {
      title : 'りっちゃんぺろぺろ',
      completed : true,
    },
    {
      title : 'あずにゃんぺろぺろ',
    },
    {
      title : 'むぎちゃんふにふに',
    },
  ]);

  var tasksView = new TasksView({collection:tasks});
  var addTaskView = new AddTaskView({collection:tasks});
  $('#tasks').html(tasksView.render().el);
})();
