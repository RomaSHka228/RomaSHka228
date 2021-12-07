package ru.mirea.kuts.clickbluttons;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private TextView tvOut;
    private Button buttonOk;
    private Button buttonCancel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvOut = (TextView) findViewById(R.id.tvOut);
        buttonOk = (Button) findViewById(R.id.button);
        buttonCancel = (Button) findViewById(R.id.button2);


        View.OnClickListener oclBtnOk = v -> tvOut.setText("Нажата кнопка ОК");
        buttonOk.setOnClickListener(oclBtnOk);
    }

    public void onClickCancelButton(View view) {
        tvOut.setText("Нажата кнопка Cancel");
        Toast.makeText(this, "Eщё один способ!", Toast.LENGTH_LONG).show();
    }
}