css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.redd.it/fwbpo1cpkcb61.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
file_path ='C:\\Users\\TEZA\\Downloads\\EV-logo.png'
logo_template ='''
<div class="chat-message user container"> 
   <div class="row">
    <div class="col-md-6">
       <img src="https://media.licdn.com/dms/image/C5603AQF1OI7dIpySdA/profile-displayphoto-shrink_400_400/0/1634469252304?e=2147483647&v=beta&t=-LYzM4ZBpKmyJf9BXnHYVL5FZtX0cq-UttE2Gnn_ygw" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;"> <span class="mx-auto" style="
    margin-left: 20px;font-weight: bold;font-size: xx-large;"> ElectroAid - Your EV Repair Advisor</span>
    </div>
  </div>
</div>
</div>
'''