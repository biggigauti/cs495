import kotlin.math.*

fun main() {
    var array1 = arrayOf(1, 2, 3, 4)
    var array2 = arrayOf(5, 6, 7, 8)
    //Initialize arrays. The idea is to import arrays for more complex calculations

    rmse(array1, array2)
}

fun rmse(obs: Array<Int>, pred: Array<Int>) { //rmse function
    if(obs.size == pred.size) { //if the size of the arrays match up, go ahead
        val diff = IntArray(pred.size) //initialize array same size as pred array
        for(i in obs.indices) {
            diff[i] = (obs[i].minus(pred[i])) //subtract each index of the arrays from each other
        }
        var mean: Double = 0.0
        for(i in diff.indices) {
            diff[i] = diff[i]*diff[i] //square each index .pow() function was stupidly confusing... why not "**" or "^"
        }
        mean = diff.average() //average the array. returns a single integer
        var squared = sqrt(mean) //square the integer. returns the "root mean squared error".

        println(squared)

        /*
        pred = predictions
        obs = observations (our actual data)

        the reason for the rmse function is to calculate the error of how far our "predicted" data
        is from our actual data.

        i use the rmse function a lot when doing data science stuff. what we'll do is build a model
        on existing data and then feed "unseen" data to that model. the rmse is the measure of
        how far from the actual (unseen) data our predicted values were.
         */
    }
}