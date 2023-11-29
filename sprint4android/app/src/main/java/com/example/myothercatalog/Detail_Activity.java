package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class Detail_Activity extends AppCompatActivity{ //con el Detail_activity mostraremos el titulo, la imagen y la descripcion de lo que seleccionemos.
    private TextView titulo;
    private ImageView imagen;
    private TextView description;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity); //aquí es donde se le pasa el layout

        Intent intent = getIntent();
        if (intent != null){
            String txt = intent.getStringExtra("titulo");
            String img = intent.getStringExtra("imagen");
            String desc = intent.getStringExtra("description");

            TextView txt_View = findViewById(R.id.Pez_txt);
            ImageView img_View = findViewById(R.id.Pez_img);
            TextView desc_View = findViewById(R.id.Pez_Description);

            txt_View.setText(txt);
            desc_View.setText(desc);

            Glide.with(this).load(img).circleCrop().into(img_View); //El glid es para que la imagen se adapte al tamaño del imageview, después cargamos la imagen, la convertimos en ciruclar y le colocamos la imagen

        }
    }
}
