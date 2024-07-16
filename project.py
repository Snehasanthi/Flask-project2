#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
     return "<div style='background:skyblue'><h1><center>A Little Help From God</center></h1><br><p>After a shipwreck, a man who was the last standing figured out how to arrive at the shore. He asked God for help. After waiting too long for God to answer his requests, he built himself a hut for his protection with destroyed bits of a shipwreck.Every day he invested a lot of energy searching for food and looking at the skyline for God's help. One day, when he returned from his food search, he found his little hut burnt to ashes. Losing all hope, he felt helpless and shouted out of anger,After a couple of hours, a boat arrived at the shore for his rescue. The man asked the captain of the ship,The Captain of the ship answered, We saw your smoke signal for help.The man's faith in God's will was re-established.</p></div>"
if __name__=='__main__':
     app.run(debug=True)     