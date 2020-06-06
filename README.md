# References

* [Referee](https://github.com/KevinBusse/cg-referee-coders-of-the-caribbean/blob/master/src/Referee.java)
    * Initial ship position 
    ```
      int xMin = 1 + j * MAP_WIDTH / shipsPerPlayer;
			int xMax = (j + 1) * MAP_WIDTH / shipsPerPlayer - 2;

			int y = 1 + random.nextInt(MAP_HEIGHT / 2 - 2);
			int x = xMin + random.nextInt(1 + xMax - xMin);
			int orientation = random.nextInt(6);
	```
    * plenty of constants to set too
* add link to cg
* [Hexagonal grid](https://www.redblobgames.com/grids/hexagons/)

# Optimization

* use map with numpy
* use bit wise operation to collect rum/mine