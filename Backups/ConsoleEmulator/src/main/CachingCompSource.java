package main;

import java.util.Map;
import java.util.List;
import java.util.HashMap;

public abstract class CachingCompSource implements CompletionSource {
	private Map<String, List<String>> cache = new HashMap<String, List<String>>();
	
	public List<String> complete(String text){
		if(cache.containsKey(text)) {
			return cache.get(text);
		} else {
			List<String> results = doCompletion(text);
			cache.put(text, results);
			return results;
		}
	}
	
	protected abstract List<String> doCompletion(String input);
}