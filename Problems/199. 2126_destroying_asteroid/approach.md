## Approach: Greedy Sorting

**1. Understand the Optimal Strategy**
To ensure the planet can destroy as many asteroids as possible, it needs to grow its mass incrementally. The most strategic way to do this is to always target the smallest available asteroids first. By absorbing smaller asteroids, the planet builds up enough mass to tackle the larger ones later.

**2. Sort the Array**
Sort the `asteroids` array in **ascending** (increasing) order. This guarantees that the planet will encounter the smallest asteroids first, maximizing its chances of survival and growth before facing the massive ones.

**3. Iterate Through the Asteroids**
Go through each asteroid in the newly sorted list one by one.

**4. Compare and Accumulate Mass**
For every asteroid, compare its mass to the current mass of the planet:
*   **Success:** If the planet's mass is greater than or equal to the asteroid's mass, the collision is successful. The asteroid is destroyed, and you add the asteroid's mass to the planet's current mass so it can continue to grow.
*   **Failure:** If the planet's mass is strictly less than the asteroid's mass, the planet is destroyed. Because the array is sorted, if the planet cannot destroy this current asteroid, it definitely won't be able to destroy any of the larger ones that follow. In this case, immediately halt the process and return false.

**5. Return the Final Result**
If the loop finishes checking every single asteroid and the planet was never destroyed, it means the planet successfully absorbed all of them. Return true.