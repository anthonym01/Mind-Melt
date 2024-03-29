package main;

import java.util.List;

public interface CompletionSource {
	public List<String> complete(String text);
}