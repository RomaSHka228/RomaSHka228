package ru.mirea.kuts.practice1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        TextView myTextView = (TextView) findViewById(R.id.textView);
        //    myTextView.setText("New Text in Mirea");
        //    Button button = findViewById(R.id.button);
        //     button.setText("MireaButton");
        //     CheckBox checkBox = findViewById(R.id.checkBox);
        //     checkBox.setChecked(true);
    }
}