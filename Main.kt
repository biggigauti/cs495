import javax.swing.*
import kotlin.system.exitProcess

fun UI() {
    //Create jframe and set size
    val f = JFrame("Calculator")
    f.setSize(300, 500)

    //Create Radiobuttons and add them to a group
    val rb1 = JRadioButton("+")
    rb1.setBounds(20, 50, 45, 30)
    val rb2 = JRadioButton("-")
    rb2.setBounds(90, 50, 40, 30)
    val rb3 = JRadioButton("*")
    rb3.setBounds(160, 50, 40, 30)
    val rb4 = JRadioButton("/")
    rb4.setBounds(230, 50, 40, 30)
    val bGroup = ButtonGroup()
    bGroup.add(rb1)
    bGroup.add(rb2)
    bGroup.add(rb3)
    bGroup.add(rb4)

    //Create text fields and j buttons
    val tf1 = JTextField()
    tf1.setBounds(10, 10, 280, 20)

    val tf2 = JTextField()
    tf2.setBounds(10, 100, 280, 20)

    val b = JButton("Calculate")
    b.setBounds(100, 150, 100, 20)

    val answer = JLabel("Enter numbers only")
    answer.setBounds(90, 180, 200, 20)

    //The action listener pulls the contents of textfield1 and textfield2 and checks which radiobutton is activated
    b.addActionListener {
        if (tf1.getText().toInt() is Int && tf2.getText().toInt() is Int) { //Grab the textfield input, convert to ints and confirm that they are ints.
            if (rb1.isSelected()) {
                answer.setText((tf1.getText().toInt().plus(tf2.getText().toInt())).toString())
            } //Turns objects into int forms, performs the math, converts them back to strings to display in answer label.
            if (rb2.isSelected()) {
                answer.setText((tf1.getText().toInt().minus(tf2.getText().toInt())).toString())
            }
            if (rb3.isSelected()) {
                answer.setText((tf1.getText().toInt().times(tf2.getText().toInt())).toString())
            }
            if (rb4.isSelected()) {
                answer.setText((tf1.getText().toInt().div(tf2.getText().toInt())).toString())
            }
        }
    }

    //Add all elements to the frame.
    f.add(rb1)
    f.add(rb2)
    f.add(rb3)
    f.add(rb4)
    f.add(tf1)
    f.add(tf2)
    f.add(b)
    f.add(answer)
    f.setLayout(null);
    f.setVisible(true);

    //Exit conditions when "X" is hit, stop the program and when the "EXIT" button is hit do the same.
    f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

    val exit = JButton("Exit")
    exit.setBounds(100, 220, 100, 20)
    exit.addActionListener { exitProcess(0) }

    f.add(exit)
}

fun main() {
    UI()
}