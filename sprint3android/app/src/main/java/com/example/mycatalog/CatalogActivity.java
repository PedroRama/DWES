package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button NavegarAlDetalle = findViewById(R.id.NavegarAlDetalle);

        NavegarAlDetalle.setOnClickListener(new View.OnClickListener() { // Agregamos un OnClick al botón
            @Override
            public void onClick(View v) {

                Intent init = new Intent(CatalogActivity.this, DetailActivity.class);// Creamos un Init para iniciar la actividad CatalogActivity
                startActivity(init); //Inicializamos el init
            }
        });
    }
}