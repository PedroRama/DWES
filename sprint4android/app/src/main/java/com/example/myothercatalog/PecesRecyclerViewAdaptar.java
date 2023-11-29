package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.List;

public class PecesRecyclerViewAdaptar  extends RecyclerView.Adapter<PecesViewHolder> { //esto es para q me muestre el adaptador
    private List<PecesData> PecesList;
    private Activity activity;

    public PecesRecyclerViewAdaptar(List<PecesData> pecesDataList, Activity activity) { //esto es para q me muestre la lista
        this.PecesList = pecesDataList;
        this.activity = activity;
    }

    @NonNull
    @Override
    public PecesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) { //esto es para q me muestre el viewholder
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.peces_viewholder, parent, false);
        return new PecesViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull PecesViewHolder holder, int position) { //esto es para q me muestre los datos
        PecesData pecesData = PecesList.get(position);
        holder.showData(pecesData, activity);
    }

    @Override
    public int getItemCount() { //esto es para q me muestre el itemcount
        return PecesList.size();
    }
}
