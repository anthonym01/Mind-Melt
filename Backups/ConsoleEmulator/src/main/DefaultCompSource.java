package main;

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class DefaultCompSource extends CachingCompSource {
	private List<String> terms;
	
	public DefaultCompSource(String...terms) {
		this(Arrays.asList(terms));
	}
	
	public DefaultCompSource(List<String> terms) {
		this.terms = terms;
	}
	
	@Override
	protected List<String> doCompletion(String input) {
		List<String> matches = new ArrayList<String>();
		for(String term : terms) {
			if(term.toLowerCase().startsWith(input.toLowerCase())) {
				matches.add(term);
			}
		}
		
		return matches;
	}
}