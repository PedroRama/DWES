package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class PecesViewHolder extends RecyclerView.ViewHolder { //esto es para q me muestre el viewholder
    private TextView textView;
    private ImageView imageView;
    private PecesData titulo;

    public PecesViewHolder(@NonNull View itemView) { //esto es para q me muestre el itemview
            super(itemView);
            textView = (TextView) itemView.findViewById(R.id.txt_celda);
            imageView = (ImageView) itemView.findViewById(R.id.img_celda);

            itemView.setOnClickListener(new View.OnClickListener() { //vamos a hacer un clicklistener con esto mostramos el itemview
                @Override
                public void onClick(View view) {
                    String name = titulo.getName();
                    Context context = view.getContext();
                    Toast.makeText(context, "Hiciste clic en el titulo: " + name, Toast.LENGTH_LONG).show();

                    Intent intent = new Intent(context, Detail_Activity.class);
                    context.startActivity(intent);
                }
            });
    }

    public void showData(PecesData data, Activity activity) { //esto es para q me muestre el showdata
        this.textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImage_url())
                .into(this.imageView);//esto es para q me muestre la imagen
        this.titulo = data;
    }
}
