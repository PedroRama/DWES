package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.widget.Toast;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;
import java.util.jar.JarException;

public class MainActivity extends AppCompatActivity {

    private Context context;
    private RequestQueue requestQueue;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); //esto es para q me muestre la pantalla
        setContentView(R.layout.activity_main); //esto es para q me muestre la pantalla

        context = this;
        requestQueue = Volley.newRequestQueue(this);
        viewRecyclerView(); //con esto mostramos la pantalla
    }

    private void viewRecyclerView() {
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;

        context = this;

        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET, //esto es para q me muestre el metodo
                "https://raw.githubusercontent.com/PedroRama/DWES/main/catalog.json", //esto es para q me muestre el json
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) { //esto es para q me muestre la respuesta
                        List<PecesData> allTheBooks = new ArrayList<>();
                        for (int i=0; i< response.length(); i++) {
                            try{
                                JSONObject libro = response.getJSONObject(i);
                                PecesData data = new PecesData(libro);
                                allTheBooks.add(data);
                            }catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }
                        PecesRecyclerViewAdaptar adapter = new PecesRecyclerViewAdaptar(allTheBooks, activity); //esto es para q me muestre el adaptador
                        recyclerView.setAdapter(adapter); //esto es para q me muestre el adaptador
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity)); //esto es para q me muestre el adaptador
                    }
                },
                new Response.ErrorListener() { //esto muestra el error
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
        );
        this.requestQueue.add(request);
    }
}