This was interesting to solve as I have never used websockets before. So the way the program works is the Chess program is run locally but the messages the fish sends is based on the move score of what you play and the fish play. When you get to the page of the game, open up the brower console and input the following:

```
queryObjects(WebSocket)
```

this will get you an array of active websocket connects, should be one object in the array, right click on the object and press "store as global variable" then type the following in the console

```
temp1.send("eval -99999999")
```

here we are sending a fake message that says we made an amazing game winning move. Flag will be in the talk bubble with the fish.